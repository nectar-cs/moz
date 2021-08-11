require 'kerbi'

class SimpleMixer < Kerbi::Mixer
  locate_self __dir__
  def run
    super do |g|
      g.yaml 'res'
    end
  end
end

kerbi.generators = [ SimpleMixer ]

puts kerbi.cli_exec